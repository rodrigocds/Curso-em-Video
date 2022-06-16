let num = [10, 8 , 7, 500, 1.5]
num[3] = 6
num.push(87) //Adiciona um elemento ao vetor
num.sort() //Ordena o vetor por ordem crescente

console.log(num)
console.log(`O vetor tem ${num.length} posições`)
console.log(`O primeiro valor do vetor é ${num[0]}`)

let pos = num.indexOf(1000) //Pesquisa se tem esse valor no vetor
if (pos == -1) { //Se o valor não for encontrado ele retornará -1
    console.log(`Nenhum valor encontrado`);
} else {
    console.log(`O valor está no posição ${pos}`)
}
