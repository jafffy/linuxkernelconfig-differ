# Kernel config differ.

## Usages
```sh
python3 kernelconfig-compare.py <config1> <config2>

# Or

python3 kernelconfig-compare.py <config1> <config2> <config1-name> <config2-name>
```

Then you could get three files,
   * A_and_B.txt
   * A_minus_B.txt
   * B_minus_A.txt

## Note
This script removes comments in linux kernel in default.

Copyright at Jaewon Choi <jaewon.james.choi@gmail.com>
