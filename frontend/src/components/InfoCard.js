import React, { useEffect } from "react";
import { marked } from "marked";
import hljs from "highlight.js"; // Importar highlight.js

const InfoCard = ({ markdownContent }) => {
    // Configurar marked para usar highlight.js
    marked.setOptions({
        highlight: (code, language) => {
            return hljs.highlightAuto(code, [language]).value;
        },
        langPrefix: "hljs language-", // Prefijo para las clases de highlight.js
    });

    // Convertir Markdown a HTML
    const htmlContent = marked(markdownContent);

    // Usar useEffect para resaltar bloques de código después de renderizar
    useEffect(() => {
        document.querySelectorAll("pre code").forEach((block) => {
            hljs.highlightElement(block);
        });
    }, [htmlContent]);

    return (
        <div
            className="info-card"
            dangerouslySetInnerHTML={{ __html: htmlContent }}
        />
    );
};

export default InfoCard;
