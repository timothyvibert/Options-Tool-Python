#!/usr/bin/env node
import { createServer } from "vite";
import { chromium } from "playwright";
import { dirname, resolve } from "path";
import { fileURLToPath } from "url";
import fs from "fs/promises";

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = resolve(__dirname, "..", "..");

const inputPath = process.argv[2];
const outputPath = process.argv[3];

if (!inputPath || !outputPath) {
  console.error(
    "Usage: node render_report.mjs <contract.json> <output.pdf>"
  );
  process.exit(1);
}

const publicDir = resolve(root, "public");
await fs.mkdir(publicDir, { recursive: true });
await fs.copyFile(
  resolve(process.cwd(), inputPath),
  resolve(publicDir, "report_contract.json")
);

const outPath = resolve(process.cwd(), outputPath);
await fs.mkdir(dirname(outPath), { recursive: true });

const server = await createServer({
  root,
  logLevel: "error",
  server: {
    port: 4173,
    strictPort: true,
  },
});

await server.listen();
const baseUrl = server.resolvedUrls?.local?.[0] ?? "http://localhost:4173";

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
await page.goto(`${baseUrl}/?contract=1`, { waitUntil: "networkidle" });
await page.emulateMedia({ media: "print" });
await page.pdf({
  path: outPath,
  format: "Letter",
  printBackground: true,
  margin: { top: "0in", right: "0in", bottom: "0in", left: "0in" },
});

await browser.close();
await server.close();
