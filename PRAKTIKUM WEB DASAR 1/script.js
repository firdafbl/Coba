var a = "Hallo Masbro" //string
var b = 10 //int
var c = 20

//cara menampilkan hasil output melalui console browser (ctrl+shift+i kemudian pilih bagian menu console)
console.log(a) //console.log = print di python
console.log(b)
console.log(b+c)
console.log("Hasil dari", b, "+", c , "=", (b+c))

//cara membuat function di javascript
function penjumlahan(a,b) {  //parameter
    return a/b //mengembalikan hasil akhir
}

console.log(penjumlahan(20, 5))  //argumen

function luaspersegipanjang() {
    var panjang = document.getElementById("panjang").value
    var lebar = document.getElementById("lebar").value
    var panjangint = parseInt(panjang)
    var lebarint = parseInt(lebar)
    var hasilnilai = panjangint * lebarint
    var hasilhtml = document.getElementById("HasilLuas")
    hasilhtml.innerHTML= "Hasil Luas Persegi Panjang dengan panjang " + panjang + " dan lebar  " + lebar + "=" + hasilnilai
}