"""
SPDX-FileCopyrightText: NVIDIA CORPORATION & AFFILIATES
Copyright (c) 2021-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

SPDX-License-Identifier: Apache-2.0
"""
load("//bzl:python.bzl", "mission_dispatch_py_library")
load("@python_third_party//:requirements.bzl", "requirement")

mission_dispatch_py_library(
    name="vda5050_types",
    srcs = glob(["*.py"]),
    deps = [
        "//:cloud_common_objects",
        requirement("pydantic")
    ],
    visibility = ["//visibility:public"]
)