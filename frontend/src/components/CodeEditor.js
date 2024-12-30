import React, { useRef } from "react";
import Prism from "prismjs";

Prism.languages.mylang = {
    comment: [
        /\/\/[^\r\n]*/,
        /\/\*[\s\S]*?\*\//
    ],
    keyword: /\b(DEFINE|SETUP|WORLD|ADD|APPEND|SCENE|INT|FLOAT|STRING|GAMEOBJECT|CHUNK|LIST)\b/,
    string: /'"' ~["]* '"'/,
    number: /\b\d+(?:\.\d+)?\b/,
    operator: /[+\-*\/=<>!]/
};

const CodeEditor = () => {
    const textareaRef = useRef(null);
    const codeRef = useRef(null);

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
