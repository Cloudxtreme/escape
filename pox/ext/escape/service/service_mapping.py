# Copyright 2015 Janos Czentye
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from escape.orchest.mapping_strategy import AbstractMappingStrategy
from escape.orchest.nffg_mapping import AbstractMapper
from escape.service import log as log


class DefaultServiceMappingStrategy(AbstractMappingStrategy):
  """
  Mapping class which maps given Service Graph into a single BiS-BiS
  """

  def __init__ (self):
    super(DefaultServiceMappingStrategy, self).__init__()

  @classmethod
  def map (cls, graph, resource):
    """

    :param graph:
    :param resource:
    :return:
    """
    log.debug(
      "Invoke mapping algorithm: %s on SG(%s)" % (cls.__name__, graph.id))
    # TODO implement
    log.debug(
      "Mapping algorithm: %s is finished on SG(%s)" % (cls.__name__, graph.id))


class ServiceGraphMapper(AbstractMapper):
  """
  Helper class for mapping Service Graph to NFFG
  """

  def __init__ (self, strategy=DefaultServiceMappingStrategy):
    super(ServiceGraphMapper, self).__init__(strategy)
    log.debug("Init %s with strategy: %s" % (
      self.__class__.__name__, strategy.__name__))

  def orchestrate (self, input_graph, resource_view):
    log.debug("Request %s to lauch orchestration on SG(%s)..." % (
      self.__class__.__name__, input_graph.id))
    # Steps before mapping (optional)
    # Run actual mapping algorithm
    nffg = self.strategy.map(graph=input_graph, resource=resource_view)
    # Steps after mapping (optional)
    log.debug("SG(%s) orchestration is finished by %s" % (
      input_graph.id, self.__class__.__name__))
    return nffg

