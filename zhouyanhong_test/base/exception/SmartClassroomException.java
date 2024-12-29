package com.smartClassroom.base.exception;

/**
 * 智慧课堂异常类
 */
public class SmartClassroomException extends RuntimeException{
    private String errCode;
    private String errMessage;
    public SmartClassroomException() {
        super();
    }

    public SmartClassroomException(String errMessage) {
        super(errMessage);
        this.errMessage = errMessage;
    }

    public SmartClassroomException(String errCode,String errMessage) {
        super(errMessage);
        this.errMessage = errMessage;
        this.errCode =errCode;
    }

    public String getErrMessage() {
        return errMessage;
    }

    public String getErrCode() {
        return errCode;
    }

    public static void cast(CommonError commonError){
        throw new SmartClassroomException(commonError.getErrMessage());
    }
    public static void cast(String errMessage){
        throw new SmartClassroomException(errMessage);
    }

    public static void err(String errCode,String errMessage){
        throw new SmartClassroomException(errCode,errMessage);
    }
}
