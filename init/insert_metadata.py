from geonetwork import GnApi

with open("init/metadata.zip", "rb") as f:
    GnApi("https://georchestra-127-0-0-1.nip.io/geonetwork/srv/api", ("testadmin", "testadmin"), False).put_record_zip(f)
