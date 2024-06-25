import mermaid from 'mermaid';

mermaid.initialize({ startOnLoad: false });

export default class GraphGenerator {

    private static _result: HTMLDivElement;

    constructor(mermaidCode: string) {
        this._mermaidCode = mermaidCode;
        if (typeof GraphGenerator._result !== 'undefined') {
            GraphGenerator._result = document.createElement('div');
            GraphGenerator._result.id = '__graph-generator-result__';
            document.body.appendChild(GraphGenerator._result);
        }
    }

    async generate(): Promise<string> {
        mermaid.initialize({ startOnLoad: false });
        const rendered = await mermaid.render('__graph-generator-result__', this._mermaidCode)
            .catch(err => console.error(err));
        if (!rendered) return '';
        return rendered.svg;
    }

    private _mermaidCode: string;

}
