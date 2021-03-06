#
# Autogenerated by Thrift Compiler (1.0.0-dev)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class SystemException(TException):
  """
  Attributes:
   - message
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'message', None, None, ), # 1
  )

  def __init__(self, message=None,):
    self.message = message

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.message = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('SystemException')
    if self.message is not None:
      oprot.writeFieldBegin('message', TType.STRING, 1)
      oprot.writeString(self.message)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __str__(self):
    return repr(self)

  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RFileMetadata:
  """
  Attributes:
   - filename
   - created
   - updated
   - deleted
   - version
   - owner
   - contentLength
   - contentHash
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'filename', None, None, ), # 1
    (2, TType.I64, 'created', None, None, ), # 2
    (3, TType.I64, 'updated', None, None, ), # 3
    (4, TType.I64, 'deleted', None, None, ), # 4
    (5, TType.I32, 'version', None, None, ), # 5
    (6, TType.STRING, 'owner', None, None, ), # 6
    (7, TType.I32, 'contentLength', None, None, ), # 7
    (8, TType.STRING, 'contentHash', None, None, ), # 8
  )

  def __init__(self, filename=None, created=None, updated=None, deleted=None, version=None, owner=None, contentLength=None, contentHash=None,):
    self.filename = filename
    self.created = created
    self.updated = updated
    self.deleted = deleted
    self.version = version
    self.owner = owner
    self.contentLength = contentLength
    self.contentHash = contentHash

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.filename = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I64:
          self.created = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.updated = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I64:
          self.deleted = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I32:
          self.version = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.STRING:
          self.owner = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I32:
          self.contentLength = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.contentHash = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RFileMetadata')
    if self.filename is not None:
      oprot.writeFieldBegin('filename', TType.STRING, 1)
      oprot.writeString(self.filename)
      oprot.writeFieldEnd()
    if self.created is not None:
      oprot.writeFieldBegin('created', TType.I64, 2)
      oprot.writeI64(self.created)
      oprot.writeFieldEnd()
    if self.updated is not None:
      oprot.writeFieldBegin('updated', TType.I64, 3)
      oprot.writeI64(self.updated)
      oprot.writeFieldEnd()
    if self.deleted is not None:
      oprot.writeFieldBegin('deleted', TType.I64, 4)
      oprot.writeI64(self.deleted)
      oprot.writeFieldEnd()
    if self.version is not None:
      oprot.writeFieldBegin('version', TType.I32, 5)
      oprot.writeI32(self.version)
      oprot.writeFieldEnd()
    if self.owner is not None:
      oprot.writeFieldBegin('owner', TType.STRING, 6)
      oprot.writeString(self.owner)
      oprot.writeFieldEnd()
    if self.contentLength is not None:
      oprot.writeFieldBegin('contentLength', TType.I32, 7)
      oprot.writeI32(self.contentLength)
      oprot.writeFieldEnd()
    if self.contentHash is not None:
      oprot.writeFieldBegin('contentHash', TType.STRING, 8)
      oprot.writeString(self.contentHash)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class RFile:
  """
  Attributes:
   - meta
   - content
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'meta', (RFileMetadata, RFileMetadata.thrift_spec), None, ), # 1
    (2, TType.STRING, 'content', None, None, ), # 2
  )

  def __init__(self, meta=None, content=None,):
    self.meta = meta
    self.content = content

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.meta = RFileMetadata()
          self.meta.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.content = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('RFile')
    if self.meta is not None:
      oprot.writeFieldBegin('meta', TType.STRUCT, 1)
      self.meta.write(oprot)
      oprot.writeFieldEnd()
    if self.content is not None:
      oprot.writeFieldBegin('content', TType.STRING, 2)
      oprot.writeString(self.content)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class NodeID:
  """
  Attributes:
   - id
   - ip
   - port
   - count
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'id', None, None, ), # 1
    (2, TType.STRING, 'ip', None, None, ), # 2
    (3, TType.I32, 'port', None, None, ), # 3
    (4, TType.I32, 'count', None, None, ), # 4
  )

  def __init__(self, id=None, ip=None, port=None, count=None,):
    self.id = id
    self.ip = ip
    self.port = port
    self.count = count

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.id = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.ip = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I32:
          self.port = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.count = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('NodeID')
    if self.id is not None:
      oprot.writeFieldBegin('id', TType.STRING, 1)
      oprot.writeString(self.id)
      oprot.writeFieldEnd()
    if self.ip is not None:
      oprot.writeFieldBegin('ip', TType.STRING, 2)
      oprot.writeString(self.ip)
      oprot.writeFieldEnd()
    if self.port is not None:
      oprot.writeFieldBegin('port', TType.I32, 3)
      oprot.writeI32(self.port)
      oprot.writeFieldEnd()
    if self.count is not None:
      oprot.writeFieldBegin('count', TType.I32, 4)
      oprot.writeI32(self.count)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
