// Capturas de prueba del visor. Uso: npm run capturas (sirve el repo en 5180 por su cuenta).
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { existsSync } from 'node:fs';

const servidor = spawn('python3', ['-m', 'http.server', '5180'], { stdio: 'ignore' });
await new Promise(r => setTimeout(r, 800));
const ruta = process.env.CHROMIUM_PATH && existsSync(process.env.CHROMIUM_PATH) ? process.env.CHROMIUM_PATH : null;
const navegador = await chromium.launch({ ...(ruta ? { executablePath: ruta } : {}), args: ['--use-gl=angle', '--use-angle=swiftshader', '--enable-unsafe-swiftshader'] });
const casos = [
  ['epoca-0100-mediterraneo', 'epoca=anio-0100&lon=18&lat=40&z=3.4'],
  ['epoca-1000-europa', 'epoca=anio-1000&lon=15&lat=45&z=3.2'],
  ['epoca-1492-europa', 'epoca=anio-1492&lon=12&lat=44&z=3.4'],
];
let fallos = 0;
try {
  for (const [nombre, q] of casos) {
    const p = await navegador.newPage({ viewport: { width: 1280, height: 720 } });
    p.on('pageerror', e => { fallos++; console.error(nombre, 'ERROR JS:', e.message); });
    p.on('console', m => { if (m.type() === 'error') { fallos++; console.error(nombre, 'ERROR consola:', m.text()); } });
    await p.goto(`http://localhost:5180/visor/index.html?${q}`);
    await p.waitForSelector('body[data-listo="1"]', { timeout: 30000 });
    await p.waitForTimeout(500);
    await p.screenshot({ path: `capturas/${nombre}.png` });
    console.log('ok', nombre);
    await p.close();
  }
} finally {
  await navegador.close();
  servidor.kill();
}
process.exit(fallos ? 1 : 0);
