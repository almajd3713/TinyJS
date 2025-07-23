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
        console.error('Error executing code:', error); 
    }
    return captured;
}

const programs = JSON.parse(fs.readFileSync(path.join('output', 'output_raw.json'), 'utf8'))

const original_console_log = console.log;
const original_console_info = console.info;

const new_programs = programs.map(program => {
    const code = program.script
    
    const captured = runIsolated(code);

    console.log('code:', code);
    console.log('Captured output:', captured);
    return {
        ...program,
        output: '# ' + captured.join('\n# ')
    }
})

fs.writeFileSync(path.join('output', 'output.json'), JSON.stringify(new_programs, null, 4), 'utf8')