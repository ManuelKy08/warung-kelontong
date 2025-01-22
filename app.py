from flask import Flask, render_template, request, redirect, url_for, session, send_from_directory
import os
import datetime
import logging

app = Flask(__name__)
app.secret_key = "kunci_rahasia"  #


def format_number(value):
    """Format angka dengan pemisah ribuan."""
    return "{:,}".format(value)

app.jinja_env.filters['format_number'] = format_number


logging.basicConfig(level=logging.DEBUG)


daftar_produk = {
    1: {"nama": "Indomie Goreng", "harga": 3000, "stok": 50, "kategori": "Makanan", "gambar": "indomie_goreng.jpg"},
    2: {"nama": "Air Mineral Aqua 600ml", "harga": 1500, "stok": 100, "kategori": "Minuman", "gambar": "aqua.jpg"},
    3: {"nama": "Roti'O", "harga": 12000, "stok": 30, "kategori": "Makanan", "gambar": "roti_o.jpg"},
    4: {"nama": "Cokelat Silverqueen", "harga": 15000, "stok": 40, "kategori": "Makanan", "gambar": "silverqueen.jpg"},
    5: {"nama": "Teh Pucuk Harum", "harga": 3500, "stok": 60, "kategori": "Minuman", "gambar": "teh_pucuk.jpg"},
    6: {"nama": "Deterjen Rinso", "harga": 18000, "stok": 20, "kategori": "Perlengkapan Rumah Tangga", "gambar": "rinso.jpg"},
    7: {"nama": "Shampo Sunsilk", "harga": 16000, "stok": 25, "kategori": "Perlengkapan Rumah Tangga", "gambar": "sunsilk.jpg"},
    8: {"nama": "Sabun Mandi Lifebuoy", "harga": 4000, "stok": 35, "kategori": "Perlengkapan Rumah Tangga", "gambar": "lifebuoy.jpg"},
    9: {"nama": "Beras Premium 5kg", "harga": 60000, "stok": 15, "kategori": "Makanan", "gambar": "beras.jpg"},
    10: {"nama": "Minyak Goreng 1L", "harga": 15000, "stok": 10, "kategori": "Makanan", "gambar": "minyak_goreng.jpg"},
    11: {"nama": "Susu Kental Manis", "harga": 10000, "stok": 45, "kategori": "Makanan", "gambar": "skm.jpg"},
    12: {"nama": "Kopi Instan", "harga": 5000, "stok": 70, "kategori": "Minuman", "gambar": "kopi.jpg"},
    13: {"nama": "Biskuit Marie", "harga": 8000, "stok": 55, "kategori": "Makanan", "gambar": "marie.jpg"},
    14: {"nama": "Mie Sedap Goreng", "harga": 2800, "stok": 80, "kategori": "Makanan", "gambar": "mie_sedap.jpg"},
    15: {"nama": "Fanta Merah", "harga": 6000, "stok": 90, "kategori": "Minuman", "gambar": "fanta.jpg"},
    16: {"nama": "Sprite", "harga": 6000, "stok": 95, "kategori": "Minuman", "gambar": "sprite.jpg"},
    17: {"nama": "Coca-Cola", "harga": 6500, "stok": 85, "kategori": "Minuman", "gambar": "coca_cola.jpg"},
    18: {"nama": " Flashdisk ", "harga": 7000, "stok": 20, "kategori": "Lain-lain", "gambar": "fd.jpg"},
    19: {"nama": " Kabel Data ", "harga": 7500, "stok": 22, "kategori": "Lain-lain", "gambar": "kabel.jpg"},
    20: {"nama": "  Headser  ", "harga": 8000, "stok": 28, "kategori": "Lain-lain", "gambar": "headset.jpg"},
    21: {"nama": "Saus Sambal", "harga": 9000, "stok": 65, "kategori": "Makanan", "gambar": "saus_sambal.jpg"},
    22: {"nama": "Kecap Manis", "harga": 9500, "stok": 60, "kategori": "Makanan", "gambar": "kecap_manis.jpg"},
    23: {"nama": "Gula Pasir 1kg", "harga": 12000, "stok": 30, "kategori": "Makanan", "gambar": "gula_pasir.jpg"},
    24: {"nama": "Garam Dapur", "harga": 2000, "stok": 75, "kategori": "Makanan", "gambar": "garam.jpg"},
    25: {"nama": "Tepung Terigu 1kg", "harga": 10000, "stok": 40, "kategori": "Makanan", "gambar": "tepung_terigu.jpg"},
    26: {"nama": "Telur Ayam 1kg", "harga": 25000, "stok": 18, "kategori": "Makanan", "gambar": "telur.jpg"},
    27: {"nama": "Tahu Putih", "harga": 3000, "stok": 50, "kategori": "Makanan", "gambar": "tahu.jpg"},
    28: {"nama": "Tempe", "harga": 2500, "stok": 55, "kategori": "Makanan", "gambar": "tempe.jpg"},
    29: {"nama": "Kerupuk Udang", "harga": 7000, "stok": 30, "kategori": "Makanan", "gambar": "kerupuk.jpg"},
    30: {"nama": "Bawang Merah", "harga": 8000, "stok": 25, "kategori": "Makanan", "gambar": "bawang_merah.jpg"},
    31: {"nama": "Teh Botol Sosro", "harga": 4000, "stok": 70, "kategori": "Minuman", "gambar": "teh_botol.jpg"},
    32: {"nama": "Nu Green Tea", "harga": 4500, "stok": 65, "kategori": "Minuman", "gambar": "nu_green_tea.jpg"},
    33: {"nama": "Sari Roti Coklat", "harga": 6000, "stok": 45, "kategori": "Makanan", "gambar": "sari_roti.jpg"},
    34: {"nama": "Wafer Tango", "harga": 10000, "stok": 50, "kategori": "Makanan", "gambar": "wafer_tango.jpg"},
    35: {"nama": "Beng-Beng", "harga": 4000, "stok": 60, "kategori": "Makanan", "gambar": "beng_beng.jpg"},
    36: {"nama": "Oreo", "harga": 9000, "stok": 55, "kategori": "Makanan", "gambar": "oreo.jpg"},
    37: {"nama": "Yakult", "harga": 8000, "stok": 80, "kategori": "Minuman", "gambar": "yakult.jpg"},
    38: {"nama": "Floridina Orange", "harga": 3000, "stok": 75, "kategori": "Minuman", "gambar": "floridina.jpg"},
    39: {"nama": "Pocari Sweat", "harga": 7000, "stok": 70, "kategori": "Minuman", "gambar": "pocari_sweat.jpg"},
    40: {"nama": "Indomie Ayam Bawang", "harga": 3000, "stok": 65, "kategori": "Makanan", "gambar": "indomie_ayambawang.jpg"},
    41: {"nama": "Super Bubur", "harga": 6000, "stok": 40, "kategori": "Makanan", "gambar": "super_bubur.jpg"},
    42: {"nama": "Energen Coklat", "harga": 2500, "stok": 50, "kategori": "Minuman", "gambar": "energen.jpg"},
    43: {"nama": "Milo Kotak", "harga": 5000, "stok": 60, "kategori": "Minuman", "gambar": "milo.jpg"},
    44: {"nama": "Susu Ultra Milk Coklat", "harga": 5500, "stok": 55, "kategori": "Minuman", "gambar": "ultra_milk.jpg"},
    45: {"nama": "Tissue Paseo", "harga": 12000, "stok": 30, "kategori": "Perlengkapan Rumah Tangga", "gambar": "paseo.jpg"},
    46: {"nama": "Pasta Gigi Pepsodent", "harga": 10000, "stok": 35, "kategori": "Perlengkapan Rumah Tangga", "gambar": "pepsodent.jpg"},
    47: {"nama": "Sikat Gigi Formula", "harga": 7000, "stok": 40, "kategori": "Perlengkapan Rumah Tangga", "gambar": "sikat_gigi.jpg"},
    48: {"nama": "Royco Ayam", "harga": 1500, "stok": 80, "kategori": "Makanan", "gambar": "royco.jpg"},
    49: {"nama": "Masako Sapi", "harga": 1500, "stok": 75, "kategori": "Makanan", "gambar": "masako.jpg"},
    50: {"nama": " sunlight ", "harga": 11000, "stok": 25, "kategori": "Perlengkapan Rumah Tangga", "gambar": "sunlight.jpg"},
    51: {"nama": " Baygon ", "harga": 20000, "stok": 15, "kategori": "Perlengkapan Rumah Tangga", "gambar": "baygon.jpg"},
    52: {"nama": " So Klin Pewangi ", "harga": 9000, "stok": 20, "kategori": "Perlengkapan Rumah Tangga", "gambar": "soklin.jpg"},
    53: {"nama": " Molto Pelembut ", "harga": 13000, "stok": 18, "kategori": "Perlengkapan Rumah Tangga", "gambar": "molto.jpg"},
}

DISKON_PEMBELIAN_BESAR = 0.05 


@app.route("/")
def index():
    return render_template("index.html", daftar_produk=daftar_produk)


@app.route("/tambah_ke_keranjang", methods=["POST"])
def tambah_ke_keranjang():
    kode_produk = request.form.get("kode_produk")
    jumlah = request.form.get("jumlah")
    app.logger.debug(f"Tambah ke keranjang - kode_produk: {kode_produk}, jumlah: {jumlah}")

    if not kode_produk or not jumlah:
        app.logger.error("kode_produk atau jumlah tidak valid")
        return redirect(url_for("index"))

    try:
        kode_produk = int(kode_produk)
        jumlah = int(jumlah)
    except ValueError as ve:
        app.logger.error(f"kode_produk atau jumlah bukan integer: kode_produk={kode_produk}, jumlah={jumlah} error = {ve}")
        return redirect(url_for("index"))

    produk = daftar_produk.get(kode_produk)
    if not produk:
        app.logger.error(f"Produk dengan kode {kode_produk} tidak ditemukan.")
        return redirect(url_for("index"))

    if jumlah > produk["stok"]:
        app.logger.error(f"Jumlah {jumlah} melebihi stok tersedia {produk['stok']}")
        return redirect(url_for("index"))

    if "keranjang" not in session:
        session["keranjang"] = {}

    if kode_produk in session["keranjang"]:
        session["keranjang"][kode_produk] += jumlah
    else:
        session["keranjang"][kode_produk] = jumlah

    app.logger.debug(f"Session setelah tambah keranjang: {session}")
    return redirect(url_for("index"))


@app.route("/keranjang")  
def lihat_keranjang():
    if "username" not in session:
        return redirect(url_for("login"))

    app.logger.debug(f"Session pada saat lihat keranjang: {session}")
    keranjang_items = []
    total_harga = 0

    if "keranjang" in session:
        app.logger.debug(f"Isi Session Keranjang: {session['keranjang']}")
        for kode, jumlah in session["keranjang"].items():
            try:
                
                kode = int(kode)
                app.logger.debug(f"Processing item - kode: {kode}, jumlah: {jumlah}, type kode: {type(kode)}")
                produk = daftar_produk.get(kode)
                if produk:
                    total_harga_item = produk["harga"] * jumlah
                    total_harga += total_harga_item
                    keranjang_items.append({
                        "kode": kode,
                        "nama": produk["nama"],
                        "harga": produk["harga"],
                        "jumlah": jumlah,
                        "total_harga": total_harga_item,
                        "gambar": produk["gambar"]
                    })
                else:
                    app.logger.error(f"produk tidak ditemukan kode = {kode}")
            except ValueError as ve:
                app.logger.error(f"kode produk bukan integer: {kode} error = {ve}")

    app.logger.debug(f"keranjang_items: {keranjang_items} total_harga {total_harga}")
    return render_template("keranjang.html", keranjang_items=keranjang_items, total_harga=total_harga)

@app.route("/update_keranjang", methods=["POST"])
def update_keranjang():
  app.logger.debug(f"Session pada saat update keranjang: {session}")
  if "keranjang" in session:
    for kode, jumlah in request.form.items():
        if kode.startswith("jumlah_"):
            try:
                produk_id = int(kode.split("_")[1])
                session["keranjang"][produk_id] = int(jumlah)
                app.logger.debug(f"Update keranjang produk_id: {produk_id} jumlah: {jumlah}")
            except ValueError:
                 app.logger.error(f"jumlah bukan integer: {jumlah}")
  return redirect(url_for("lihat_keranjang"))

@app.route("/hapus_dari_keranjang/<int:kode_produk>")
def hapus_dari_keranjang(kode_produk):
    app.logger.debug(f"Session pada saat hapus dari keranjang: {session} kode_produk = {kode_produk}")
    if "keranjang" in session and kode_produk in session["keranjang"]:
        del session["keranjang"][kode_produk]
    return redirect(url_for("lihat_keranjang"))


@app.route("/checkout")
def checkout():
    if "username" not in session:
        return redirect(url_for("login"))

    app.logger.debug(f"Session pada saat checkout: {session}")
    if "keranjang" not in session or not session["keranjang"]:
        return redirect(url_for("index"))  

    keranjang_items = []
    total_belanja = 0
    for kode, jumlah in session["keranjang"].items():
      try:
        kode = int(kode)
        produk = daftar_produk.get(kode)
        if produk:
            total_harga_item = produk["harga"] * jumlah
            total_belanja += total_harga_item
            keranjang_items.append({
                "kode": kode,
                "nama": produk["nama"],
                "harga": produk["harga"],
                "jumlah": jumlah,
                "total_harga": total_harga_item,
                "gambar": produk["gambar"]
            })
        else:
            app.logger.error(f"produk tidak ditemukan kode = {kode}")
      except ValueError as ve:
           app.logger.error(f"kode produk bukan integer: {kode} error = {ve}")

    diskon = 0
    if total_belanja > 100000:
        diskon = total_belanja * DISKON_PEMBELIAN_BESAR

    total_bayar = total_belanja - diskon

    return render_template("checkout.html", keranjang_items=keranjang_items, total_belanja=total_belanja, diskon=diskon, total_bayar=total_bayar)

@app.route("/proses_pembayaran", methods=["POST"])
def proses_pembayaran():
    app.logger.debug(f"Session pada saat proses pembayaran: {session}")
    if "keranjang" not in session or not session["keranjang"]:
        return redirect(url_for("index"))

    total_belanja = 0
    for kode, jumlah in session["keranjang"].items():
        try:
            kode = int(kode)
            produk = daftar_produk.get(kode)
            if produk:
                total_belanja += produk["harga"] * jumlah
        
                if produk["stok"] >= jumlah:
                    daftar_produk[kode]["stok"] -= jumlah
                else:
                     app.logger.error(f"Stok tidak mencukupi. kode: {kode} stok: {produk['stok']} jumlah:{jumlah}")
                     return redirect(url_for("lihat_keranjang"))  
            else:
                app.logger.error(f"produk tidak ditemukan kode = {kode}")
        except ValueError as ve:
           app.logger.error(f"kode produk bukan integer: {kode} error = {ve}")
           return redirect(url_for("lihat_keranjang"))
    diskon = 0
    if total_belanja > 100000:
        diskon = total_belanja * DISKON_PEMBELIAN_BESAR

    total_bayar = total_belanja - diskon

    
    if "riwayat_transaksi" not in session:
        session["riwayat_transaksi"] = []
    transaksi = {
        "waktu": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "produk": [{"nama": daftar_produk[int(kode)]["nama"], "jumlah": jumlah} for kode, jumlah in session["keranjang"].items() if daftar_produk.get(int(kode))],
        "total_bayar": total_bayar
    }
    session["riwayat_transaksi"].append(transaksi)

    
    session.pop("keranjang", None)


    app.logger.info(f"Pembayaran berhasil. Total bayar: {total_bayar}")
    return render_template("pembayaran_berhasil.html", total_bayar=total_bayar)

@app.route("/riwayat_transaksi")
def riwayat_transaksi():
    if "username" not in session:
        return redirect(url_for("login"))

    riwayat = session.get("riwayat_transaksi", [])
    return render_template("riwayat_transaksi.html", riwayat=riwayat)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profil")
def profil():
    if "username" not in session:
        return redirect(url_for("login"))
    return render_template("profil.html")

@app.route("/proses_login", methods=["POST"])
def proses_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'user' and password == 'pass':
        session['username'] = username
        return redirect(url_for('index'))
    else:
        return render_template("login.html", error="Invalid credentials")


@app.route("/logout")
def logout():
    session.pop('username', None)
    session.pop('profile_picture', None)
    return redirect(url_for('index'))

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/proses_register", methods=["POST"])
def proses_register():
    username = request.form['username']
    password = request.form['password']
    
    session["username"] = username
    return redirect(url_for('index'))

@app.route('/upload-profile-picture', methods=['POST'])
def upload_profile_picture():
    if 'profile_picture' not in request.files:
        return redirect(url_for('profil'))
    
    file = request.files['profile_picture']

    if file.filename == '':
        return redirect(url_for('profil'))

     
    file_path = os.path.join('static/images', file.filename)
    file.save(file_path)


    session['profile_picture'] = url_for('static', filename='images/' + file.filename)
   
    return redirect(url_for('profil'))

if __name__ == "__main__":
    app.run(debug=True)