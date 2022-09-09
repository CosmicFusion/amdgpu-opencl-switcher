Name:          amdgpu-opencl-switcher
Version:       1.1
Release:       0%{?dist}
License:       GPL
Group:         Unspecified
Summary:       Select needed OpenCL implementation with cl_pro prefix


Source0:        %{name}-%{version}-%{release}.x86_64.tar.gz

URL:           https://github.com/CosmicFusion/amdgpu-opencl-switcher






Provides:      amdgpu-opencl-switcher = %{version}-%{release}
Provides:      amdgpu-opencl-switcher(x86-64) = %{version}-%{release}
Requires:      /usr/bin/bash

%install
tar -xf %{SOURCE0}
mv usr %{buildroot}/

%description
Select needed opencl implementation with cl_pro prefix
%files
%attr(0755, root, root) "/usr/bin/cl_pro"
%attr(0644, root, root) "/usr/share/bash-completion/completions/cl_pro"

