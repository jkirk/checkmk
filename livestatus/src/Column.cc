// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#include "Column.h"

#include <cassert>
#include <iterator>
#include <utility>

#include "Logger.h"

Column::Column(std::string name, std::string description, Offsets offsets)
    : _logger(Logger::getLogger("cmk.livestatus"))
    , _name(std::move(name))
    , _description(std::move(description))
    , _offsets(std::move(offsets)) {}

const void *Column::shiftPointer(Row row) const {
    return _offsets.shiftPointer(row.rawData<void>());
}

Column::Offsets::Offsets(std::initializer_list<int> offsets) {
    for (const int *it = begin(offsets); it != end(offsets); ++it) {
        if (it == std::prev(end(offsets))) {
            final_offset_ = *it;
        } else if (*it >= 0) {
            indirect_offsets_.push_back(*it);
        }
    }
}

Column::Offsets Column::Offsets::addIndirectOffset(int offset) const {
    assert(!final_offset_);
    Offsets result{*this};
    if (offset >= 0) {
        result.indirect_offsets_.push_back(offset);
    }
    return result;
}

Column::Offsets Column::Offsets::addFinalOffset(int offset) const {
    assert(!final_offset_);
    Offsets result{*this};
    if (offset >= 0) {
        result.final_offset_ = offset;
    }
    return result;
}

const void *Column::Offsets::shiftPointer(const void *data) const {
    for (auto i : indirect_offsets_) {
        // TODO(sp) Figure out what is actually going on regarding nullptr...
        if (data == nullptr) {
            return nullptr;
        }
        data = *offset_cast<const void *>(data, i);
    }
    if (data == nullptr) {
        return nullptr;
    }
    return offset_cast<const void>(data, final_offset_.value_or(0));
}
