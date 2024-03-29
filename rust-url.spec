%bcond_without check
%global debug_package %{nil}

%global crate url

Name:           rust-%{crate}
Version:        2.2.1
Release:        2
Summary:        URL library for Rust, based on the WHATWG URL Standard

# Upstream license specification: MIT/Apache-2.0
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/url
Source:         %{crates_source}
# Initial patched metadata
# * Exclude CI files, https://github.com/servo/rust-url/pull/467
Patch0:         url-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
URL library for Rust, based on the WHATWG URL Standard.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%license LICENSE-MIT LICENSE-APACHE
%{cargo_registry}/%{crate}-%{version_no_tilde}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages
which use "serde" feature of "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{cargo_registry}/%{crate}-%{version_no_tilde}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 15 2020 Josh Stone <jistone@redhat.com> - 2.1.1-1
- Update to 2.1.1

* Sun Aug 25 08:50:10 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.1.0-1
- Update to 2.1.0

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 00:12:03 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.2-4
- Regenerate

* Sun Mar 10 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.2-3
- Do not pull optional dependencies

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Nov 13 2018 Josh Stone <jistone@redhat.com> - 1.7.2-1
- Update to 1.7.2

* Sat Nov 03 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.1-5
- Adapt to new packaging

* Sat Jul 28 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.1-4
- Rebuild to trigger tests

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jul 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.1-2
- Do not ignore test results

* Fri Jul 06 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.1-1
- Update to 1.7.1

* Tue Mar 13 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.0-2
- Bump rustc-test to 0.3

* Wed Feb 21 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.7.0-1
- Update to 1.7.0

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 08 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-2
- Rebuild for rust-packaging v5

* Fri Nov 10 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.6.0-1
- Initial package
