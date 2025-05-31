let biblioteca = [];

function cadastrar_livro(titulo, autor){
    let livro = {
      titulo: titulo, 
      autor: autor,
      status: "disponivel"

}


biblioteca.push(livro);
console.log("livro cadastrado com sucesso!")
}

function listar_livros(){

 if (biblioteca.length ==0){
   console.log("nenhum livro cadastrado ainda. ");
 } else {
   console.log("lista de livros cadastrados:\n");


   for (let i = 0; i < biblioteca.length; i++){
    let livro = biblioteca[i];

    console.log("livro" + (i+1));
    console.log("titulo:" + livro.titulo);
    console.log("autor:" + livro.autor);
    console.log("status: " + livro.status);
     console.log("-----------------------------");
   }
  }
}

function buscar_livro(tituloprocurado) {
    let encontrado = false;

    for(let i = 0; i < biblioteca.length; i++) {

      if (biblioteca[i].titulo === tituloprocurado){
        console.log(" livro encontrado");
        console.log("tiutlo:" + biblioteca[i].titulo);
        console.log("autor:" + biblioteca[i].autor);
        console.log("status:"+ biblioteca[i].status)
        encontrado = true;
        break;
      }
    }
}


if(encontrado) {

  console.log("livro nao encontrado");

}


function alterar_status(tituloprocurado) {

 let encontrado = false;

 for (let i =0; i < biblioteca.length; i++) {

   if (biblioteca[i].titulo === tituloprocurado) {
    encontrado = true;


    if(biblioteca[i].status === "disponivel") {
     biblioteca[i].status = "emprestado";
     console.log(` o livro "${biblioteca[i].titulo}" foi emprestado com sucesso`);
    }else{
     biblioteca[i].status = "disponivel";
     console.log(` o livro "${biblioteca[i].titulo}" foi devolvido e esta disponivel`);
    }
    break;
   }
  }

  if (encontrado) {
    console.log("livro nao encontrado");
  }
}