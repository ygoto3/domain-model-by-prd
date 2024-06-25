import GraphGenerator from './GraphGenerator';

async function main() {
    const prdTitle = document.querySelector('#prd-title') as HTMLTextAreaElement;
    const prdTextarea = document.querySelector('#prd-editor') as HTMLTextAreaElement;
    const submitButton = document.querySelector('#submit') as HTMLButtonElement;
    const mermaidImg = document.querySelector('#mermaid') as HTMLImageElement;
    const loadingIndicator = document.querySelector('#loading-indicator') as HTMLDivElement;
    const prdsSelect = document.querySelector('#prds') as HTMLSelectElement;

    window.addEventListener('load', onLoad);
    prdsSelect.addEventListener('change', onSelect);
    submitButton.addEventListener('click', onSubmit);

    async function onLoad(ev: Event) {
        const result = await fetch(`${process.env.API_ORIGIN}/v1/prds`)
            .then(res => res.json());
        result.forEach((prd: any) => {
            const option = document.createElement('option');
            option.value = prd.id;
            option.text = prd.title;
            prdsSelect.appendChild(option);
        });
    }

    async function onSelect(ev: Event) {
        const prdId = prdsSelect.value;
        if (prdId === '0') return;
        const result = await fetch(`${process.env.API_ORIGIN}/v1/prds/${prdId}`)
            .then(res => res.json());
        prdTitle.value = result.title;
        prdTextarea.value = result.body;
        if (result.mermaid.indexOf('classDiagram\n') !== 0) {
            mermaidImg.innerHTML = '';
            return;
        }
        const graphGenerator = new GraphGenerator(result.mermaid);
        const svg = await graphGenerator.generate();
        mermaidImg.innerHTML = svg;
    }

    async function onSubmit(ev: MouseEvent) {
        ev.preventDefault();
        try {
            loadingIndicator.style.display = 'block';
            const result = await fetch(`${process.env.API_ORIGIN}/v1/prds`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ title: prdTitle.value, body: prdTextarea.value }),
            })
            .then(res => res.json());

            if (result.mermaid.indexOf('classDiagram\n') === 0) {
                const graphGenerator = new GraphGenerator(result.mermaid);
                const svg = await graphGenerator.generate();
                mermaidImg.innerHTML = svg;
            }
        } catch (err) {
            console.error(err);
        } finally {
            loadingIndicator.style.display = '';
        }
    }
}
  
main();
