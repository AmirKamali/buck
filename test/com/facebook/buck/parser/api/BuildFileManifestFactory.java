/*
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package com.facebook.buck.parser.api;

import com.facebook.buck.util.collect.TwoArraysImmutableHashMap;
import com.google.common.collect.ImmutableList;
import com.google.common.collect.ImmutableMap;
import com.google.common.collect.ImmutableSortedSet;
import java.util.Map;
import java.util.Optional;

public class BuildFileManifestFactory {

  private BuildFileManifestFactory() {}

  public static BuildFileManifest create(
      ImmutableMap<String, ImmutableMap<String, Object>> targets) {
    return ImmutableBuildFileManifest.of(
        targets.entrySet().stream()
            .collect(
                TwoArraysImmutableHashMap.toMap(
                    Map.Entry::getKey, e -> TwoArraysImmutableHashMap.copyOf(e.getValue()))),
        ImmutableSortedSet.of(),
        ImmutableMap.of(),
        Optional.empty(),
        ImmutableList.of(),
        ImmutableList.of());
  }
}
