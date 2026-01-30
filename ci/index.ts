import path from "node:path"
import * as readline from 'node:readline/promises';
import * as fs from 'node:fs';

const CHANGED_FILES = process.env.CHANGED_FILES!
let ARRAY_CHANGED_FILES = CHANGED_FILES.split("\n")

for (const filename of ARRAY_CHANGED_FILES) {
    let extension = path.extname(filename)
    let allow = [".cls", ".int", ".csp", ".mac"]
    let isNotExtensionAllow = (!allow.includes(extension))

    if (isNotExtensionAllow) {
        continue
    }

    await readLine(filename)
}

async function readLine(filename: string): Promise<void> {
    const stream = fs.createReadStream(filename);
    const read = readline.createInterface({input: stream, crlfDelay: Infinity});

    read.on('line', (line) => {
        console.log(`Linha do arquivo: ${line}`);
    });

    await new Promise((resolve) => read.on('close', resolve));
}