let amigo = {
    nome: 'José',
    sexo: 'M',
    peso: 85.4,
    engordar(p=0) {
        console.log('Engordou')
        this.peso += p
    }
}
console.log(`${amigo.nome} pesava ${amigo.peso}Kg`)
amigo.engordar(10)
console.log(`Agora ele pesa ${amigo.peso}Kg`)