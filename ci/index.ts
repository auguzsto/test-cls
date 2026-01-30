import path from "node:path"
import * as readline from 'node:readline/promises';
import * as fs from 'node:fs';

const CHANGED_FILES = process.env.CHANGED_FILES!;
let ARRAY_CHANGED_FILES = CHANGED_FILES.split("\n");

for (const filename of ARRAY_CHANGED_FILES) {
    let extension = path.extname(filename);
    let allow = [".cls", ".int", ".csp", ".mac"];
    let isNotExtensionAllow = (!allow.includes(extension));

    if (isNotExtensionAllow) {
        continue
    }

    const content = returnContentInArray(filename);
    console.log(content)
}

function returnContentInArray(filename: string): Array<string> {
    const result: Array<string> = [];
    const stream = fs.createReadStream(filename);
    const read = readline.createInterface({input: stream, crlfDelay: Infinity});

    read.on('line', (line) => {
        result.push(line)
    });

    return result;
}