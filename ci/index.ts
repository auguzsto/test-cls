import path from "node:path"

const CHANGED_FILES = process.env.CHANGED_FILES!
let ARRAY_CHANGED_FILES = CHANGED_FILES.split("\n")

for (const filename of ARRAY_CHANGED_FILES) {
    let extension = path.extname(filename)
    let allow = [".cls", ".int", ".csp", ".mac"]
    let isNotExtensionAllow = (!allow.includes(extension))

    if (isNotExtensionAllow) {
        continue
    }

    console.log(filename)
}