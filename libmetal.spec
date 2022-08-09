Name:		libmetal
Version:	2022.04.0
Release:	2
Summary:	An abstraction layer across user-space Linux, baremetal, and RTOS environments

License:	BSD
URL:		https://github.com/OpenAMP/libmetal/
Source0:	https://github.com/OpenAMP/libmetal/archive/v%{version}/%{name}-%{version}.tar.gz

Patch0:		libmetal-add-additional-arches.patch

BuildRequires:	cmake
BuildRequires:	doxygen
BuildRequires:	gcc
BuildRequires:	glibc-devel
BuildRequires:	libsysfs-devel

%description
An abstraction layer across user-space Linux, baremetal, and RTOS environments.

%package devel
Summary: 	Development files for libmetal
Requires:	%{name}%{?_isa} = %{version}-%{release}
%description devel
Development file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.

%package doc
Summary:	Documentation files for libmetal
BuildArch:	noarch
%description doc
Documentation file for libmetal: An abstraction layer across user-space Linux,
baremetal, and RTOS environments.


%prep
%autosetup -p1


%build
mkdir build
cd build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DWITH_STATIC_LIB=OFF -DWITH_EXAMPLES=ON ..


%install
cd build
%make_install
for f in `find %{buildroot}/%{_bindir}/ -type f -regex ".*-shared*"`; do
    newf="`echo ${f} | sed 's/-shared*$//g'`"
    mv "${f}" "${newf}"
done


%ldconfig_scriptlets

%files
%license LICENSE.md
%doc README.md
%{_libdir}/*.so*
%{_bindir}/test-*

%files devel
%{_libdir}/libmetal.so
%{_includedir}/metal/

%files doc
%license LICENSE.md
%doc README.md
%doc %{_datarootdir}/doc/metal/


%changelog
* Fri Aug 5 2022 zhangziyang <zhangziyang1@huawei.com> - 2022.04.0-2
- synchronous embedded compilation and packaging options

* Thu Jun 30 2022 luojects <luoyonglun@huawei.com> - 2022.04.0-1
- update to 2022.04.0

* Sat Feb 12 2022 Wayne Ren <renwei41@huawei.com> - 2021.10.0-1
- update to 2021.10.0

* Tue Dec 14 2021 konglidong <konglidong@uniontech.com> - 2020.10.0-2
- delete %dist

* Tue Jan 26 2021 Zhenyu Zheng <zheng.zhenyu@outlook.colm> - 2020.10.0-1
- Initial commit for openEuler

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2020.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Nov  2 20:02:29 GMT 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.10.0-1
- Update to 2020.10.0

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.0-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2020.04.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun May 10 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.04.0-1
- Update to 2020.04.0

* Thu Mar 05 2020 Peter Robinson <pbrobinson@fedoraproject.org> - 2020.01.0-1
- Update to 2020.01.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Peter Robinson <pbrobinson@fedoraproject.org> 2018.10-1
- Update to 2018.10 release

* Sun Oct 14 2018 Peter Robinson <pbrobinson@fedoraproject.org> 2018.04-1
- Update to 2018.04 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2017.10-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 20 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-4
- Add patch to build on other arches

* Mon Feb 19 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-3
- Make -doc subpackage a noarch package

* Sat Feb 17 2018 Jared Smith <jsmith@fedoraproject.org> - 2017.10-2
- Fix up issues identified in package review

* Tue Feb 13 2018 Jared K. Smith <jsmith@fedoraproject.org> - 2017.10-1
- Initial packaging
