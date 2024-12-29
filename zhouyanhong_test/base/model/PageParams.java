package com.smartClassroom.base.model;

import io.swagger.annotations.ApiModelProperty;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class PageParams {
    @ApiModelProperty("当前页码")
    private Long pageNo= 1L;
    @ApiModelProperty("最大当前页数")
    private Long pageSize=10L;
}
