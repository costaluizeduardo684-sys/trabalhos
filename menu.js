/* ==========================================================================
   MENU DO SITE (aparece em todas as páginas) — edite só esta lista.

   texto : nome que aparece embaixo do ícone
   icone : classe do ícone do Bootstrap Icons (veja todos em icons.getbootstrap.com)
           ex.: "bi-house-door-fill", "bi-cart-fill", "bi-heart-fill"
   link  : uma página do seu site  -> "pag2.html"
           ou um site de fora      -> "https://www.exemplo.com.br"
                                      (abre em outra aba)

   Para mudar um ÍCONE, troque o valor de "icone".
   Para colocar um SITE no botão, troque o valor de "link".
   Pode ter mais ou menos botões: a barra se ajusta sozinha.
   ========================================================================== */
const MENU = [
  { texto: "Início",   icone: "bi-house-door-fill",      link: "index.html" },
  { texto: "Carrinho", icone: "bi-cart-fill",            link: "pag2.html"  },
  { texto: "Ofertas",  icone: "bi-bag-fill",             link: "pag3.html"  },
  { texto: "Perfil",   icone: "bi-person-fill",          link: "pag4.html"  },
  { texto: "Ajuda",    icone: "bi-question-circle-fill", link: "pag5.html"  },
];

/* ------------------- daqui para baixo não precisa mexer ------------------- */
(function () {
  const arquivo = location.pathname.split("/").pop() || "index.html";
  let ativo = MENU.findIndex((m) => m.link === arquivo);
  if (ativo < 0) ativo = 0;

  const ehExterno = (l) => /^https?:\/\//i.test(l);

  const itens = MENU.map((m, i) => `
    <li class="lista${i === ativo ? " ativo" : ""}">
      <a href="${m.link}"${ehExterno(m.link) ? ' target="_blank" rel="noopener"' : ""}>
        <span class="icone"><i class="bi ${m.icone}"></i></span>
        <span class="texto">${m.texto}</span>
      </a>
    </li>`).join("");

  const nav = document.createElement("div");
  nav.className = "navegacao";
  nav.setAttribute("role", "navigation");
  nav.innerHTML = `<ul style="width:${MENU.length * 70}px">${itens}<div class="indicador" style="--i:${ativo}"></div></ul>`;
  document.body.appendChild(nav);

  const lista = nav.querySelectorAll(".lista");
  const indicador = nav.querySelector(".indicador");
  const reduzir = matchMedia("(prefers-reduced-motion: reduce)").matches;

  lista.forEach((li, i) => {
    li.addEventListener("click", (e) => {
      const a = li.querySelector("a");
      const href = a.getAttribute("href");
      if (ehExterno(href)) return;                       // site de fora: abre em outra aba
      if (e.ctrlKey || e.metaKey || e.shiftKey) return;  // abrir em nova aba do jeito normal
      e.preventDefault();
      if (href === "#") return;

      lista.forEach((x) => x.classList.remove("ativo"));
      li.classList.add("ativo");
      indicador.style.setProperty("--i", i);
      setTimeout(() => (location.href = a.href), reduzir ? 0 : 350); // deixa a animação aparecer
    });
  });
})();
