# wallet_owner
checks if BTC wallet is private or part of an exchange/mixer

This script is written as a Maltego transform.

Upon receiving a BTC address, the script cheks the address on 'https://vivigle.com/' to learn if the address is connected to an exchange, mixer or if it is a private wallet.

If it is conneced to and exchange/mixer, the Maltego BTC address entity will be recreated with a purple bookmark and a note with name of the exchange or the word 'mixer' if it is connected to a mixer.

If the address is connected to a private wallet, the Maltego BTC adreess entity will be recreated witha a yellow bookmark.

Note, the website 'vivigle.com' is a preliminary free version of the company 'Chain Analysis'.  The database used is not fully updated and results from the website are not always accurate.  To get more accurate results, one would have to purchase a subscription from Chain Analysis or a simuilar company.
