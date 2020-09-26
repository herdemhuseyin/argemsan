frappe.ui.form.on("Purchase Order", {
	//The trigger can be changed, but refresh must be used to use a button
	refresh: function(frm) {
        var strDoctype = frm.doctype;
        var strDocName = frm.doc.name;
		//The following line creates a button.
		frm.add_custom_button(__("Dosya Eklerini Al"),
			//The function below is triggered when the button is pressed.
			function() {
                msgprint(strDoctype);
                msgprint(strDocName);               
//*- Döngünün başladığı yer.
                $.each(frm.doc.items,  function(i,  d) {
                    var StrStokkodu = d.item_code;
                    msgprint(StrStokkodu);                                

                    frappe.db.get_value("File", {"attached_to_doctype":"Item", "attached_to_name":StrStokkodu}, "*", function(value) {
                      //msgprint(value.file_url);
                      if (value.attached_to_name = StrStokkodu){
                        msgprint("Ekli dosya Var");
                        msgprint(value.attached_to_name);
                      }else{
                         msgprint("Dosya Eki Yok");
                        }                     
                    });

                    // if (frappe.db.exists({
                    //   'doctype': 'File',
                    //   'attached_to_doctype': 'Item',
                    //   'attached_to_name': StrStokkodu})){
                    //     msgprint("Dosya Eki Var");
                    //   }  

                        
                });
               // frm.refresh_field('items'); 	



                
//*-
		});
	}
});