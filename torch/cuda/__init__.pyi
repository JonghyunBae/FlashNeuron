from typing import Optional, Tuple, Union
from .. import device as _device

def is_available() -> bool: ...
def init() -> None: ...

class cudaStatus:
    SUCCESS: int
    ERROR_NOT_READY: int

class CudaError:
    def __init__(self, code: int) -> None: ...

class _CudaDeviceProperties:
    name: str
    major: int
    minor: int
    multi_processor_count: int
    total_memory: int
    is_integrated: int
    is_multi_gpu_board: int

_device_t = Union[_device, int]

def check_error(res: int) -> None: ...
def device_count() -> int: ...
def empty_cache() -> None: ...
def synchronize(device: _device_t) -> None: ...
def set_device(device: _device_t) -> None: ...
def get_device_capability(device: Optional[_device_t]=...) -> Tuple[int, int]: ...
def get_device_name(device: Optional[_device_t]=...) -> str: ...
def get_device_properties(device: _device_t) -> _CudaDeviceProperties: ...
def current_device() -> int: ...
def memory_allocated(device: Optional[_device_t]=...) -> int: ...
def max_memory_allocated(device: Optional[_device_t]=...) -> int: ...
def reset_max_memory_allocated(device: Optional[_device_t]=...) -> None: ...
def memory_cached(device: Optional[_device_t]=...) -> int: ...
def max_memory_cached(device: Optional[_device_t]=...) -> int: ...
def reset_max_memory_cached(device: Optional[_device_t]=...) -> None: ...
def set_rng_state(new_state): ...
def get_rng_state(): ...
def FN_setting(flags: int) -> None: ...
