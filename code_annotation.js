import fs from 'fs'
import path from 'path'
import vm from 'vm'

const runIsolated = (code) => {
    const captured = [];
    const sandbox = {
        console: {
            log: (...args) => {
                captured.push(...args);
            },
            info: (...args) => {
                captured.push(...args);
            }
        }
    };
    const ctx = vm.createContext(sandbox);
    try {
        vm.runInContext(code, ctx);
    } catch (error) {
        return false 
    }
    return captured;
}

const programs = JSON.parse(fs.readFileSync(path.join('output', 'output_raw.json'), 'utf8'))

const new_programs = programs.map(program => {
    const code = program.script
    
    const captured = runIsolated(code);

    if (!captured) return;
    return {
        ...program,
        output: '# ' + captured.join('\n# ')
    }
}).filter(program => program !== undefined);

console.log(programs.length - new_programs.length, 'programs were dropped');

fs.writeFileSync(path.join('output', 'output.json'), JSON.stringify(new_programs, null, 4), 'utf8')