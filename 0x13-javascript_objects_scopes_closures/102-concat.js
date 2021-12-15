#!/usr/bin/node
const fs = require('fs');
const fc = process.argv[4];
const ta = fs.readFileSync(process.argv[2], 'utf8');
const tb = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(fc, ta + tb);
