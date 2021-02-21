document.addEventListener("DOMContentLoaded", function () {
  console.info("Document complètement chargé");
});

document.addEventListener("DOMContentLoaded", () => {
  // va chercher tous les éléments avec la classe "column"
  const $columns = document.querySelectorAll(".column");

  // pour chacun (même si ici il n'y en a qu'un seul)
  $columns.forEach((column) => {
    column.addEventListener("click", () => {
      // on va lire l'attribut "data-target"
      const target = column.dataset.target;
      // on ajoute un handler
      column.addEventListener("click", () => {
        console.log(`Vous avez cliqué sur l'image ${target} à ${Date.now()}`);
      });
    });
  });
});
