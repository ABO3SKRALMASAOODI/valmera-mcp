import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import { readFile, mkdir, rm } from 'node:fs/promises';
import { createServer } from 'node:http';
import { resolve } from 'node:path';
import { setTimeout as hold } from 'node:timers/promises';
import { chromium } from 'playwright';

const output = resolve(process.argv[2] ?? './localhost-demo-output');
await mkdir(output, { recursive: true });
const fixture = await readFile(new URL('./preview.html', import.meta.url));
const server = createServer((request, response) => {
  if (request.url !== '/') {
    response.writeHead(404).end();
    return;
  }
  response.writeHead(200, { 'Content-Type': 'text/html; charset=utf-8', 'Cache-Control': 'no-store' });
  response.end(fixture);
});
await new Promise((ready, reject) => server.once('error', reject).listen(0, '127.0.0.1', ready));
const origin = `http://127.0.0.1:${server.address().port}`;
let browser;

try {
  browser = await chromium.launch({ channel: 'chrome' });
  for (const [name, clickSave, expected] of [
    ['01-selection-only', false, 'Saved schedule: Monthly'],
    ['02-selection-saved', true, 'Saved schedule: Weekly'],
  ]) {
    const frame = { width: 1024, height: 576 };
    const context = await browser.newContext({ viewport: frame, recordVideo: { dir: output, size: frame } });
    const page = await context.newPage();
    const video = page.video();
    try {
      await page.goto(origin);
      const saved = page.getByRole('status');
      assert.equal(await saved.textContent(), 'Saved schedule: Monthly');
      await hold(800);
      const input = page.getByRole('combobox', { name: 'Digest schedule' });
      await input.selectOption('Weekly');
      assert.equal(await input.inputValue(), 'Weekly');
      await hold(550);
      if (clickSave) await page.getByRole('button', { name: 'Save changes' }).click();
      assert.equal(await saved.textContent(), expected);
      await page.screenshot({ path: resolve(output, `${name}.png`), animations: 'disabled' });
      await hold(1750);
    } finally {
      await context.close();
    }
    const webm = await video.path();
    execFileSync(process.env.FFMPEG ?? 'ffmpeg', [
      '-hide_banner', '-loglevel', 'error', '-y', '-i', webm,
      '-an', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', resolve(output, `${name}.mp4`),
    ]);
    await rm(webm);
    console.log(`${name}: ${expected}`);
  }
} finally {
  await browser?.close();
  await new Promise(ready => server.close(ready));
}
