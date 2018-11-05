
Java.perform(function() {
	
	//Interceptor.attach (Module.findExportByName("libName.so", "FuntionName"), {
	Interceptor.attach (Module.findExportByName("/lib/arm/libgame.so", "criAtomConfig_GetMd5Hash"), {
		onEnter: function (args) {   
			//console.log("hi")
		},
		onLeave: function (retval) {
			//console.log("in " +retval);
			//retval.replace(0x25);
			console.log(retval+" out");
		
		}
		});

});   