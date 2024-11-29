import React, { useState } from 'react';

const ProgramInput = () => {

    const [program, setProgram] = useState(
        `// Write your code here...\nDEFINE SETUP(){\n\n}\n\nDEFINE WORLD("Example"){\n\n}`);

    return (
        <div className='program-input-container'>
            <textarea
                className='program-input-textarea'
                spellCheck='false'
                value={program}
                onChange={(e) => setProgram(e.target.value)}
            />
            <button className='program-input-button' >Generate</button>
        </div>
    );
};

export default ProgramInput;
