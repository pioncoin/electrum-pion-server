# Main network and testnet3 definitions

# Pion src/chainparams.cpp
params = {
    'pion_main': {
        'pubkey_address': 55, #P
        'script_address': 48, #L
        'genesis_hash': '000009c77e1208a736b8289762416db2472b644e35fe8341104e1de218673a0d' 
    },
    'pion_test': {
        'pubkey_address': 118, # p
        'script_address': 125, # s 
        'genesis_hash': '000006b4dac951b8df45f31c642dbfc9591e801bad467cedeb0e07498cbe2554' 
    }
}
