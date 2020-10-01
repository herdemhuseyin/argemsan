//Stok Fişleri Ekranında Lot Oluşturma Kodları
frappe.ui.form.on("Stock Entry Detail", "lot_olustur", function(frm, cdt, cdn) {
    //msgprint("Yeni Bir Lot Numarası Oluşturuldu. Lütfen Kontrol Ederek Seçiniz."); 
    var strItemCode = frappe.model.get_value(cdt, cdn, "item_code");
    //Malzeem kartında lot takibi var mı kontrol edelim
    frappe.db.get_value("Item", strItemCode, "has_batch_no", function(value) {
        //console.log(value);
        if (value.has_batch_no == 1) {
            msgprint("Lot Takibi Var")
            //Bu isimde lot var mı kontrol edelim
            var strlotaciklamasi = frappe.model.get_value(cdt, cdn, "lot_aciklamasi");

            frappe.db.get_value("Batch", {"item": strItemCode, "lot_aciklamasi": strlotaciklamasi}, "*", function(objResult) {
                //msgprint(value.file_url);
                if (objResult.lot_aciklamasi == strlotaciklamasi) {
                    frappe.model.set_value(cdt, cdn, "batch_no", objResult.name);
                    msgprint("İlgili Lot Nosu Seçildi.");
                } else {
                    msgprint("Lot Kaydı Bulunamadı yenisi açıldı.");
	                const batch = frappe.model.get_new_doc("Batch");
		            batch.item = frappe.model.get_value(cdt, cdn, "item_code");
                    batch.lot_aciklamasi = frappe.model.get_value(cdt, cdn, "lot_aciklamasi");

                    frappe.db.insert(batch).then(function(doc) { 
                        console.log(`${doc.doctype} ${doc.name} created on ${doc.creation}`);
                        frappe.model.set_value(cdt, cdn, "batch_no", doc.name);
                    });


                  }                     
              });


        } else {
            msgprint("Bu stok kartında lot takibi yapılmamaktadır.");
        }
    });    
    })