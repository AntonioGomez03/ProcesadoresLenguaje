import React, { useRef, useEffect } from "react";
import Prism from "prismjs";

Prism.languages.mylang = {
    comment: [
        /\/\/[^\r\n]*/,
        /\/\*[\s\S]*?\*\//
    ],
    keyword: /\b(DEFINE|SETUP|WORLD|ADD|APPEND|SCENE|INT|FLOAT|STRING|GAMEOBJECT|CHUNK|LIST)\b/,
    string: /"[^"]*"/,
    number: /\b\d+(?:\.\d+)?\b/,
    operator: /[+\-*\/=<>!]/
};

const CodeEditor = () => {
    const textareaRef = useRef(null);
    const codeRef = useRef(null);

    const initialCode = `DEFINE SETUP(){
    /* Definición del setup */
    GAMEOBJECT global_object1 = GAMEOBJECT("'src/models/tree'", 10, 2.0);
    LIST<GAMEOBJECT> global_objects = [global_object1];

    /* Definición de los chunks */
    CHUNK global_chunk1 =  CHUNK(0,0,20.0, 7.5, "src/textures/grass", global_objects);
}

DEFINE WORLD("Mi mundo"){
    /* Definición de escena */
    DEFINE SCENE("Escena 1"){
        /* Definición de objetos */
        GAMEOBJECT object1 = GAMEOBJECT("'src/models/tree'", 10, 2.0);
        LIST<GAMEOBJECT> objects = [object1];

        /* Definición de chunks */
        LIST<CHUNK> chunks
        FOR i FROM 0 TO 10{
            CHUNK c = CHUNK(i,0,20.0, 7.5, "src/textures/grass", objects);
            APPEND chunks c;
        }

        /* Agregar los chunks a la escena */
        FOR c IN chunks{
            ADD c;
        }
        
        /* Agregar un chunk global */
        ADD global_chunk1
    }
}
     `;

    const update = (text) => {
        const resultElement = codeRef.current;
        if (text[text.length - 1] === "\n") {
            text += " ";
        }
        resultElement.innerHTML = text
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;");
        Prism.highlightElement(resultElement);
    };

    const syncScroll = (element) => {
        const parent = codeRef.current.parentElement;
        parent.scrollTop = element.scrollTop;
        parent.scrollLeft = element.scrollLeft;
    };

    const syncScrollReverse = (element) => {
        const textarea = textareaRef.current;
        textarea.scrollTop = element.scrollTop;
        textarea.scrollLeft = element.scrollLeft;
    };

    const handleKeyDown = (event) => {
        const element = textareaRef.current;
        if (event.key === "Tab") {
            event.preventDefault();
            const code = element.value;
            const beforeTab = code.slice(0, element.selectionStart);
            const afterTab = code.slice(element.selectionEnd);
            const cursorPos = element.selectionStart + 1;
            element.value = `${beforeTab}\t${afterTab}`;
            element.selectionStart = cursorPos;
            element.selectionEnd = cursorPos;
            update(element.value);
        }
    };

    useEffect(() => {
        const textarea = textareaRef.current;
        textarea.value = initialCode;
        update(initialCode);
    }, []);

    return (
        <div className="code-editor-div">
            <textarea className="code-editor-textarea"
                ref={textareaRef}
                spellCheck="false"
                onInput={(e) => update(e.target.value)}
                onScroll={(e) => syncScroll(e.target)}
                onKeyDown={handleKeyDown} />
            <pre className="code-editor-pre"
                onScroll={(e) => syncScrollReverse(e.target)}>
                <code ref={codeRef} className="language-mylang"></code>
            </pre>
        </div>
    );
};

export default CodeEditor;
