import ixmp
import message_ix.testing

print(ixmp.__version__)
print(message_ix.__version__)

mp = ixmp.Platform(dbtype='HSQLDB')
message_ix.testing.make_westeros(mp, emissions=True, solve=False)
