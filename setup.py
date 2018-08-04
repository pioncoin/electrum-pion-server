from setuptools import setup

setup(
    name="electrum-pion-server",
    version="1.0",
    scripts=['run_electrum_pion_server','electrum-pion-server'],
    install_requires=['plyvel','jsonrpclib', 'irc >= 11, <=14.0', 'x16r_hash'],
    package_dir={
        'electrumserver':'src'
        },
    py_modules=[
        'electrumserver.__init__',
        'electrumserver.utils',
        'electrumserver.storage',
        'electrumserver.deserialize',
        'electrumserver.networks',
        'electrumserver.blockchain_processor',
        'electrumserver.server_processor',
        'electrumserver.processor',
        'electrumserver.version',
        'electrumserver.ircthread',
        'electrumserver.stratum_tcp'
    ],
    description="Pion Electrum Server",
    author="Thomas Voegtlin ,ELM4ever, Propulsion, TheLazieR, pioncore",
    author_email="thomasv@electrum.org, thelazier@gmail.com, info@pioncoin.org",
    license="MIT Licence",
    url="https://github.com/spesmilo/electrum-server/ , https://github.com/thelazier/electrum-pion-server/, https://github.com/dashpay/electrum-dash-server/",
    long_description="""Server for the Electrum Lightweight Pion Wallet"""
)
