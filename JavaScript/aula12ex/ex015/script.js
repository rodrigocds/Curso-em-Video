function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fAno = document.querySelector('#txtano')
    var res = document.querySelector('#res')

    if (fAno.value.length == 0  || fAno.value > ano) {
        alert('Verifique os dados e tente novamente!')
    } else {
        var fSex = document.querySelectorAll('[name="radsex"]')
        var idade = ano - Number(fAno.value)
        res.innerHTML = `Idade calculada: ${idade}`
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id', 'foto')
        if (fSex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 10) {
                //Criança
                img.setAttribute('src', './img/foto-bebe-m.jpg')
            } else if (idade < 20) {
                //Jovem
                img.setAttribute('src', './img/foto-jovem-m.jpg')
            } else if (idade < 50) {
                //Adulto
                img.setAttribute('src', './img/foto-adulto-m.jpg')
            } else {
                //Idoso
                img.setAttribute('src', './img/foto-idoso-m.jpg')
            }
        } else {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                //Criança
                img.setAttribute('src', './img/foto-bebe-f.jpg')
            } else if (idade < 20) {
                //Jovem
                img.setAttribute('src', './img/foto-jovem-f.jpg')
            } else if (idade < 50) {
                //Adulto
                img.setAttribute('src', './img/foto-adulto-f.jpg')
            } else {
                //Idoso
                img.setAttribute('src', './img/foto-idoso-f.jpg')
            }
        }
        res.style.textAlign = 'center'
        res.innerHTML = `Detectamos ${genero} com ${idade} anos <br>`
        res.appendChild(img)
    }
}