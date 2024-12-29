package com.smartClassroom.base.exception;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.io.Serializable;

/**
 * 和前端约定返回的异常信息模型
 */
@Data

@NoArgsConstructor
public class RestErrorResponse implements Serializable {
  private String errCode;
  private String errMessage;

  public RestErrorResponse(String errCode, String errMessage) {
    this.errCode = errCode;
    this.errMessage = errMessage;
  }

  public RestErrorResponse(String errMessage) {
    this.errMessage = errMessage;
  }
}
