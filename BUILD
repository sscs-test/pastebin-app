# load("@rules_python//python:defs.bzl", "py_binary")
# load("@py_deps//:requirements.bzl", "requirement")
#  
# # py_runtime(
# #     name = "python3_runtime",
# #     path = "/usr/local/bin/python",
# #     visibility = ["//visibility:public"],
# # )
# #
# # py_runtime_pair(
# #     name = "py_runtime_pair",
# #     py2_runtime = None,
# #     py3_runtime = ":python3_runtime",
# # )
# #
# # toolchain(
# #     name = "py_3_toolchain",
# #     toolchain = ":py_runtime_pair",
# #     toolchain_type = "@bazel_tools//tools/python:toolchain_type",
# # )
#
# py_binary(
#   name = "app",
#   srcs = ["app.py"],
#   deps = [
#       requirement("flask"),
#       requirement("flask-httpauth")
#   ]
# )

load("@rules_python//python:defs.bzl", "py_binary")
load("@my_deps//:requirements.bzl", "requirement")

py_binary(
  name = "app",
  srcs = ["app.py"],
  deps = [
      requirement("flask"),
      requirement("flask-httpauth")
  ]
)
