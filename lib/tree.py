class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
      return self._dfs(self.root,id)
    
  def _dfs(self, node, node_id):
        if node['id'] == node_id:
            return node
        for child in node['children']:
            result = self._dfs(child, node_id)
            if result:
                return result
        return None
