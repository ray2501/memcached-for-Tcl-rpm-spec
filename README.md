# memcached-for-Tcl-rpm-spec
openSUSE RPM spec for memcached-for-Tcl

這是一個用來建立 memcached-for-Tcl openSUSE RPM 的 spec。

## libmemcached-devel

在 openSUSE 上使用 zypper 安裝：

	sudo zypper in libmemcached libmemcached-devel libsasl2-3

## memcached-for-Tcl

[memcached-for-Tcl](https://github.com/bovine/memcached-for-Tcl) 運用 rpm spec，
透過 rpmbuild 或者是其它相關的工具建立一個 RPM 檔案以後來安裝。
