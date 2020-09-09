// Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
// This file is part of Checkmk (https://checkmk.com). It is subject to the
// terms and conditions defined in the file COPYING, which is part of this
// source code package.

#ifndef Column_h
#define Column_h

#include "config.h"  // IWYU pragma: keep

#include <chrono>
#include <cstddef>
#include <functional>
#include <initializer_list>
#include <memory>
#include <optional>
#include <string>
#include <vector>

#include "Filter.h"
#include "Row.h"
#include "contact_fwd.h"
#include "opids.h"
class Aggregation;
class Aggregator;
class Logger;
class RowRenderer;

template <typename T>
const T *offset_cast(const void *ptr, size_t offset) {
    // cppcheck is too dumb to see that this is just pointer arithmetic... :-/
    // cppcheck-suppress invalidPointerCast
    return reinterpret_cast<const T *>(reinterpret_cast<const char *>(ptr) +
                                       offset);
}

enum class ColumnType { int_, double_, string, list, time, dict, blob, null };

using AggregationFactory = std::function<std::unique_ptr<Aggregation>()>;

class Column {
public:
    class Offsets {
    public:
        // NOTE: google-explicit-constructor forbids an 'explicit' here.
        // cppcheck-suppress noExplicitConstructor
        Offsets(std::initializer_list<int> offsets);
        [[nodiscard]] Offsets addIndirectOffset(int offset) const;
        [[nodiscard]] Offsets addFinalOffset(int offset) const;
        const void *shiftPointer(const void *data) const;

    private:
        std::vector<int> indirect_offsets_;
        std::optional<int> final_offset_;
    };

    Column(std::string name, std::string description, Offsets);
    virtual ~Column() = default;

    [[nodiscard]] std::string name() const { return _name; }
    [[nodiscard]] std::string description() const { return _description; }

    template <typename T>
    [[nodiscard]] const T *columnData(Row row) const {
        return static_cast<const T *>(shiftPointer(row));
    }

    [[nodiscard]] virtual ColumnType type() const = 0;

    virtual void output(Row row, RowRenderer &r, const contact *auth_user,
                        std::chrono::seconds timezone_offset) const = 0;

    [[nodiscard]] virtual std::unique_ptr<Filter> createFilter(
        Filter::Kind kind, RelationalOperator relOp,
        const std::string &value) const = 0;

    [[nodiscard]] virtual std::unique_ptr<Aggregator> createAggregator(
        AggregationFactory factory) const = 0;

    [[nodiscard]] Logger *logger() const { return _logger; }

private:
    Logger *const _logger;
    std::string _name;
    std::string _description;
    Offsets _offsets;

    [[nodiscard]] const void *shiftPointer(Row row) const;
};

#endif  // Column_h
