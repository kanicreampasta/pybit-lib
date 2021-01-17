#include "pybit.h"

std::vector<unsigned char> bits_from_float(float a)
{
    const auto *ptr = reinterpret_cast<const unsigned char*>(&a);
    std::vector<unsigned char> bytes;
    for (size_t i=0; i<sizeof(float); i++)
    {
        bytes.push_back(ptr[i]);
    }
    return bytes;
}

std::vector<unsigned char> bits_from_float_add(float a, float b)
{
    return bits_from_float(a + b);
}
