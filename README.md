This script will help you to convert a json dictionary fed to stdin to a set of bash exports.
The following command will make json dictionary key/value pairs as environment variables in the current shell process:

```bash
echo '{"foo": "bar"}' | js2sh.py
export foo=bar

eval `echo '{"foo": "bar"}' | js2sh.py` 
echo $foo
bar

eval `js2sh.py < myconfig.json`
```
