function volumekubus() {
    var panjang = document.getElementById("panjang").value
    var lebar = document.getElementById("lebar").value
    var tinggi = document.getElementById("tinggi").value
    var panjangint = parseInt(panjang)
    var lebarint = parseInt(lebar)
    var tinggiint = parseInt(tinggi)
    var hasilnilai = panjangint * lebarint * tinggiint
    var hasilhtml = document.getElementById("HasilVolume")
    hasilhtml.innerHTML= "Hasil volume kubus" + " = " + hasilnilai
}
 
function luaskubus() {
    var sisi1 = document.getElementById("sisi1").value
    var sisi2 = document.getElementById("sisi2").value
    var sisi1int = parseInt(sisi1)
    var sisi2int = parseInt(sisi2)
    var hasilnilai = 6 * sisi1int * sisi2int 
    var hasilhtml = document.getElementById("HasilLuas")
    hasilhtml.innerHTML= "Hasil luas kubus" + " = " + hasilnilai
} 


