import frida, sys, pefile


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


PACKAGE_NAME = "PackageName"


jscode= """
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
"""
try:
    process = frida.get_usb_device().attach(PACKAGE_NAME)
    script = process.create_script(jscode)
    script.on('message', on_message)
    print('[*] Running Hook')
    script.load()
    sys.stdin.read()
except Exception as e:
    print(e)
