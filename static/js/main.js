class FormContainer extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.innerHTML = `
      <main id="${this.id}"> 
      <slot></slot> 
      </main>
    `;
    }
}
customElements.define('form-container', FormContainer);


class NavBar extends HTMLElement {
    constructor() {
        super();

        this.render = this.render.bind(this);
        this.render();
        this.optionButtons = this.shadowRoot.querySelectorAll('.option_button');
        this.optionButtons.forEach(optionButton =>
            optionButton.addEventListener('click', this.handleClick)
        );
    }
    handleClick(e) {
        const selected = e.target.textContent;
        const container = document.querySelector('#display-field');
        container.setAttribute('selected', selected);
    }
    options() {
        let options = data;
        return Object.keys(options).map(option => {
            return `
      <li value="${option}" class="nav_option">
      <button class="option_button" onclick="this.handleClick">${option}</button>
      </li>`;
        }).join('');
    }
    render() {
        const shadowRoot = this.shadowRoot || this.attachShadow({ mode: 'open' });
        shadowRoot.innerHTML = `
    <ol id="${this.id}" class="nav_bar">
    ${this.options()}
    </ol>
    `;
    }
}
customElements.define('nav-bar', NavBar);

class Display extends HTMLElement {
    constructor() {
        super();
        const shadowRoot = this.attachShadow({ mode: 'open' });
        shadowRoot.innerHTML = `
    <div id="display" class="display">${this.setSelected()}</div>
    `;
        this.display = this.shadowRoot.querySelector('#display');
    }

    static get observedAttributes() {
        return ['selected'];
    }
    attributeChangedCallback() {
        this.display.innerHTML = this.setSelected();
    }

    setSelected() {
        const key = this.getAttribute('selected');
        const dataLength = data.options[key] ? data.options[key].length : 0;
        const randomNumber = Math.floor(Math.random() * Math.floor(dataLength));
        const selected = data.options[key] ? data.options[key][randomNumber] : '';
        return selected ? selected : 'Choose an author';
    }
}