QUERY_WIQL="""SELECT
    [System.Id],
    [System.WorkItemType],
    [System.Title],
    [Custom.Client],
    [Custom.Project],
    [Custom.ProjectName],
    [System.AssignedTo],
    [System.State]
FROM workitems
WHERE
    [System.TeamProject] = @project
    AND [System.AreaPath] = @project
    AND (
        [System.WorkItemType] = 'Bug'
        OR [System.WorkItemType] = 'Product Backlog Item'
    )
    AND [System.State] <> ''
    AND [Custom.Client] <> ''
"""